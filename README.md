Avro schema for FHIR DSTU3
==========================

Initial avro schema for DSTU3 FHIR and example how to load the schema, 
validate the resources, and store parsed FHIR jsons into avro format.

Implemented resources:

    Generic:
        * Batch
        * Coding
        * Period
        * Policy
        * Position
        * Quantity
        * Range
        * Address
        * Attachment
        * Codeableconcept
        * Contactpoint
        * HumanName
        * Ratio
        * Repeat
        * Communication
        * Idetifier
        * Reference
        * SampleData
        * Timing
        * Udi
        * Actor
        * Administration
        * Annotation
        * AvailableTime
        * Collection
        * Communication
        * DateCriterion
        * DoseAndRate
        * FocalDevice
        * NotAvailable
        * Nutrient
        * PackageConcent
        * Processing
        * Protocol
        * ReactionRef
        * ReferenceRange
        * Supplement
        * Texture
        * Component
        * Contact
        * Container
        * Data
        * Diagnosis
        * DispenseRequest
        * Dosage
        * EnteralFormula
        * Evidence
        * Except
        * Explanation
        * Hospitalization
        * Link
        * OralDiet
        * Package
        * Participant
        * Performer
        * PractitionerRef
        * Qualification
        * QuestionaireAnswerOption
        * QuestionaireEnableWhen
        * QuestionaireInitial
        * QuestionaireItem
        * QuestionaireAnswer
        * Reaction
        * Recommendation
        * Related
        * Requester
        * Stage
        * StatusHistory
        * Substition
        * Target
        * UsageContext
        * VaccinationProtocol
        
    FHIR Resources:
        * AllergyIntolerance
        * Appointment
        * Bundle
        * Condition
        * Consent
        * Coverate
        * Device
        * DeviceRequest
        * DeviceUsesStatement
        * DiagnosticReport
        * Encounter
        * Flag
        * Goal
        * Immunization
        * ImmunizationRecommendation
        * Ingredient
        * Location
        * Medication
        * MedicationAdministration
        * MedicationDispense
        * MedicationStatement
        * NutritionOrder
        * Observation
        * Organization
        * Patient
        * Practitioner
        * PractitionerRole
        * Procedure
        * ProcedureRequest
        * Questionnaire
        * QuestionnaireResponse
        * Specimen* Questionnaire
        
### Run example:

```bash
virtualenv --python=python3 venv
. venv/bin/activate
pip install -r requirements.txt
python process_fhir_to_avro.py
```

