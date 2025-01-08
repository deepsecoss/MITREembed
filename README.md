# MITREembed

**Map MITRE ATT&CK techniques to n-dimensional embeddings and vice versa.**

MITREembed is designed to enhance the context and usability of machine learning (ML) or artificial intelligence (AI)-based anomaly detection outputs by mapping them to MITRE ATT&CK techniques. This project enables deeper insights into cybersecurity detection results by providing contextual translations of numerical outputs into understandable and actionable information. 

While several existing tools focus on writing and mapping to MITRE ATT&CK from sources such as SIGMA, Splunk, Snort IDS rules, YAML, and Python:
- They could benefit from more visibility.
- They often lack the ability to integrate with deep learning-based anomaly detection systems.

## Purpose

The key innovation in this project is the ability to bridge the gap between ML/AI anomaly detection outputs and actionable cybersecurity insights. By embedding MITRE techniques in a vector database and leveraging advanced search methods, MITREembed allows for:
1. Translating deep learning-based anomaly detection outputs into meaningful, human-readable formats (e.g., mapping a score or weight to a MITRE technique).
2. Enhancing detection workflows by providing relevant context and cross-referenced documentation for identified anomalies.

## Project Flow

MITREembed consists of several components that work together to map detection data to MITRE techniques and provide actionable outputs:

### Data Collection
- **Sources**: Includes SIGMA rules, Splunk, Snort IDS, and other detection rules.
- **Input Types**: Supports multiple formats (e.g., YAML, JSON, and Python scripts).

### ETL (Extract, Transform, Load)
- Collects and processes security detection rules and logs.
- Converts the data into vectorized embeddings.

### Vector Database Storage
- Stores the vectorized data for efficient search and retrieval.
- Utilizes multi-vector search techniques to match queries with relevant MITRE techniques and security detections.

### LLM Integration
- Leverages a local Large Language Model (LLM) to provide contextual answers and insights.
- Maps detection data to MITRE ATT&CK techniques and cross-references with relevant documentation.

### Local Installation and Usage
- Designed for local installation, ensuring data privacy and security.
- Provides a user-friendly interface for cybersecurity analysts to interact with the system.

## **RAG: The Foundation of MITREembed**

Retrieval-Augmented Generation (RAG) is the backbone of MITREembed, combining Large Language Models (LLMs) with vector databases to deliver contextually accurate and evidence-based insights. This foundational technology ensures the system provides actionable answers grounded in authoritative sources like MITRE ATT&CK techniques and cybersecurity regulations.

#### **Why RAG Matters**
- **Contextual Precision**: Links AI-generated responses to authoritative data, ensuring reliable insights.
- **Scalability**: Handles large datasets efficiently using vector databases for fast and accurate retrieval.
- **Flexibility**: Adapts to diverse data sources, including Splunk logs, Sigma rules, and YAML configurations.
- **Empowerment**: Enhances decision-making by automating tedious tasks and providing detailed, cross-referenced answers.

RAG enables MITREembed to dynamically adapt to new regulations, detection frameworks, and emerging cybersecurity needs, transforming it into an intelligent and transparent advisor for cybersecurity analysts.

## Example Use Case

### Cybersecurity Analyst Workflow
1. **Query**: The analyst submits a Splunk detection rule for mapping to a MITRE technique.
   - Example: `Convert this Splunk detection rule into a MITRE ATT&CK technique`
2. **Process**: 
   - The system processes the rule through the vector database using multi-vector search.
   - The LLM cross-references stored documents and retrieves relevant MITRE techniques.
3. **Response**: 
   - The output provides a detailed mapping to a MITRE ATT&CK technique, along with cross-referenced documentation.
   - Example: `The MITRE ATT&CK technique associated with RDP or Remote Desktop Protocol, commonly known as port 3389, is "Remote Services: Remote Desktop Protocol" (T1021).`

### Visual Representation
#### Figure 1: Workflow Diagram
![MITREembed Workflow](https://github.com/deepsecoss/MITREembed/assets/7229755/b2437797-4055-4e80-b021-58ffe003551d)

#### Figure 2: ETL to Local Deployment
![ETL to LLM Integration](https://github.com/deepsecoss/MITREembed/assets/7229755/54c7d129-f40a-4c04-82c7-6f14c2275233)

## Benefits
- **Enhanced Context**: Translates ML anomaly scores into actionable cybersecurity insights mapped to MITRE techniques.
- **Customizable**: Allows for integration into local infrastructures, ensuring privacy and adaptability.
- **Empowers Analysts**: Provides a seamless interface for querying, cross-referencing, and understanding detection rules and their implications.

## Future Work
- Integrate additional ML anomaly detection models.
- Expand support for more security tools and input formats.
- Optimize embeddings for faster query responses.

## License
MITREembed is released under a Apache License.

## Contributions
We welcome contributions to expand the capabilities of MITREembed. Please submit pull requests or reach out to the maintainers for more information.

---

