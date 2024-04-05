import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/path/to/your/sigma_mitre.csv')

# Define a function to convert 'tags' into URLs for the 'filename' column
def convert_to_url_final(tags):
    for tag in tags:
        if tag.startswith('attack.'):
            # Split the tag into parts
            parts = tag.split('.')
            if parts[1].startswith('t'):  # Checks if it's in the 'tXXXX' format
                # Handles both 'tXXXX' and 'tXXXX.YYY' formats
                technique = parts[1].upper()  # Convert to uppercase 'T'
                if len(parts) == 2:  # If no subtechnique
                    return f"https://attack.mitre.org/techniques/{technique}/"
                elif len(parts) == 3:  # If there's a subtechnique
                    return f"https://attack.mitre.org/techniques/{technique}/{parts[2]}/"
    return None

# Convert string representation of lists to actual lists
df['tags'] = df['tags'].apply(eval)

# Apply the conversion function to create the 'filename' column
df['filename'] = df['tags'].apply(convert_to_url_final)

# Save the DataFrame with the new 'filename' column to a CSV file
df.to_csv('/path/to/your/sigma_mitre_corrected.csv', index=False)
