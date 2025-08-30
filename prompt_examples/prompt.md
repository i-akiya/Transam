/no_think
### Role
You are an expert of CDISC biomedical concept curating.

### Goal
Generate CDISC biomedical concept regarding "NSCLC-SAQ Version 1.0 - Appetite Domain Subscore" in YAML format that matches the exact structure shown below.

### Step‑by‑Step Instructions

1. 'packageDate' – set this node to 'null' (leave it empty).

2. 'packageType' – set this node to 'bc'.

3. 'conceptId'
   Retrieve the detailed information for NCI concepts of "NSCLC-SAQ Version 1.0 - Appetite Domain Subscore" using nci concept tool in first.
   And then, set this node to 'code' value in the retrieved json

4. 'ncitCode' - set this node to 'code' value in the retrieved json.

5. 'href' - set this node to concatinate url text "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=" and 'code' value in the retrieved json.

6. 'parentConceptId' - set this node to 'parents' value in the retrieved json.

7. 'categories' - find information about categories of "NSCLC-SAQ Version 1.0 - Appetite Domain Subscore" using the document retriever tool in first, and then infer possible high‑level categories for this CDISC biomedical concept from the definition (and any other descriptive information) of the NCI concept and information from the document retriever tool, One or more categories are permitted.

8. 'shortName' - set this node to 'name' value in the retrieved json.

9. 'synonyms' – set this node to 'synonyms' value in the retrieved json.

10. 'resultScales' - find information about result value of "NSCLC-SAQ Version 1.0 - Appetite Domain Subscore" in first, and then infer possible result scale from Quantitative, Ordinal, Nominal, and Narrative.
Valid Result Scale entries are:
- Quantitative: Numeric values such as integers and decimal results
- Ordinal: Qualitative result that has a natural ordering, e.g., dipstick results 0, 1+, 2+, 3+, 4+
- Nominal: Qualitative result with no natural ordering, e.g., color of eyes
- Narrative: Free text

11. 'definition' - set this node to 'definition' value in the retrieved json.

12. 'dataElementConcepts' - if name or definition in the retrived json includes the word of questionnaire, 'dataElementConcepts' have to include "Ordinal Position", "Clinical or Research Assessment Answer", "Category", "Subcategory", "Completion Status", "Not-Done Reason", "Evaluator", and "Collection Date Time" as 'shorName'
  - 'conceptId' - Retrieve the detailed information for NCI concepts of the above 'shorName' using nci concept tool in first.
   And then, set this node to 'code' value in the retrieved json.
  - 'ncitCode' - set this node to 'code' value in the retrieved json.
  - 'href' - set this node to concatinate url text "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=" and 'code' value in the retrieved json.
  - 'shortName' - set this node to 'name' value in the retrieved json.
  - 'dataType' - infer a data type from boolean, date, datetime, decimal, integer, string, duration, and uri.
  - 'exampleSet' - This is a list of example data. infer plausible example values (or an empty list if uncertain) based on information the retrieved json, or the document retriever tool.


### Output Requirement

- Produce a single, valid YAML document that follows the structure of the example above and incorporates all information gathered from steps 1‑12.
- Ensure proper indentation, correct YAML syntax, no extraneous text, and without any yaml comments.

When completed, return only the YAML content.

### Example of a Valid CDISC Biomedical Concept (YAML)
Do not generate same data and information from the following example.

```yaml
packageDate:
packageType: bc
conceptId: C94535
ncitCode: C94535
href: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C94535
parentConceptId: C50995
categories:
  - Response Evaluation Criteria in Solid Tumors
  - Response Evaluation Criteria in Solid Tumors Version 1.1
  - Disease Response Assessment Test
  - Disease Response
  - RECIST 1.1
  - Non-Target
shortName: Response in Non‑Target Lesion
synonyms:
  - NTRGRESP
  - Non‑Target Response
resultScales:
  - Nominal
definition: "A qualitative or quantitative measurement of the response of a non‑target lesion(s) to the therapy."
dataElementConcepts:
  - conceptId: C117388
    ncitCode: C117388
    href: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C117388
    shortName: Disease Response Category
    dataType: string
    exampleSet:
      - "RECIST 1.1"
  - conceptId: C117221
    ncitCode: C117221
    href: https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C117221
    shortName: Original Result or Finding
    dataType: string
    exampleSet:
      - "NON‑CR/NON‑PD"
      - "PD"
      - "CR"
      - "NE"
```
