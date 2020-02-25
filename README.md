Avro schema for FHIR DSTU3
==========================

Initial avro schema for DSTU3 FHIR and example how to load the schema, 
validate the resources, and store parsed FHIR jsons into avro format.

Implemented resources:

    Generic:
        * batch
        * coding
        * period
        * position
        * quantity
        * range
        * codeableconcept
        * ratio
        * repeat
        * idetifier
        * timing
        * doseandrate
        * reference
        * annotation
        * diagnosis
        * dosage
        * participant
        * performer
        * qualification
        * questionnaire fields
        * reaction
        * referencerange
        * sampledata
        * stage
        * substition
        * target
        * usagecontext
        
    FHIR Resources:
        * AllergyIntolerance
        * Bundle
        * Condition
        * DiagnosticReport
        * Encounter
        * Goal
        * Ingredient
        * Location
        * Medication
        * MedicationAdministration
        * MedicationDispense
        * MedicationStatement
        * Observation
        * Organization
        * Patient
        * Practitioner
        * Procedure
        * Questionnaire
        
### Run example:

```bash
virtualenv --python=python3 venv
. venv/bin/activate
pip install -r requirements.txt
python process_fhir_to_avro.py
```

