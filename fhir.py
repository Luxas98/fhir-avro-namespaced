examples = {
    "AllergyIntolerance": """{
        "resourceType": "AllergyIntolerance",
        "id": "bdb58da4-2394-4396-b641-3d8eb1142d18",
        "clinicalStatus": "active",
        "verificationStatus": "confirmed",
        "type": "allergy",
        "category": [
          "food"
        ],
        "criticality": "low",
        "code": {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "419474003",
              "display": "Allergy to mould"
            }
          ],
          "text": "Allergy to mould"
        },
        "patient": {
          "reference": "Patient/5a7dc54cf2f5f10100361927"
        },
        "assertedDate": "1994-06-30T19:17:36+00:00"
      }""",
    "Patient": """{
                "resourceType": "Patient",
                "identifier": [
                    {
                        "use": "usual",
                        "type": {
                            "coding": [
                                {
                                    "system": "http://loinc.org",
                                    "code": "76435-7"
                                }
                            ]
                        },
                        "value": "5a7dc54cf2f5f10100361927"
                    }
                ],
                "gender": "male",
                "birthDate": "1980-01-01",
                "managingOrganization": {
                    "reference": "Organization/MyOrganization"
                }
            }""",
    "Observation": """{
                        "resourceType": "Observation",
                        "status": "final",
                        "code": {
                          "coding": [
                          {
                            "system": "http://loinc.org",
                            "code": "8480-6"
                          }
                          ]
                        },
                        "subject": {
                          "reference": "Patient/5a7dc54cf2f5f10100361927"
                        },
                        "effectiveDateTime": "2010-09-12T12:16:17+00:00",
                        "valueQuantity": {
                          "value": 120,
                          "system": "http://unitsofmeasure.org",
                          "code": "mm[Hg]"
                        }
                      }""",
    "Encounter": """{
        "resourceType": "Encounter",
        "id": "8b4b0a06-61bf-41e1-8aab-3acf5b6bc750",
        "status": "finished",
        "class": {
          "code": "inpatient"
        },
        "type": [
          {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "305411003",
                "display": "Admission to thoracic surgery department"
              }
            ],
            "text": "Admission to thoracic surgery department"
          }
        ],
        "subject": {
          "reference": "Patient/5a7dc54cf2f5f10100361927"
        },
        "period": {
          "start": "1988-10-04T03:07:26+00:00",
          "end": "1988-10-05T03:22:26+00:00"
        },
        "reason": [
          {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "185086009",
                "display": "Chronic obstructive bronchitis (disorder)"
              }
            ]
          }
        ]
      }
    """,
    "Procedure": """{
        "resourceType": "Procedure",
        "id": "96e2bfbe-4c65-44e9-9c3c-0321ab317cee",
        "status": "completed",
        "code": {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "429609002",
              "display": "Lung volume reduction surgery (procedure)"
            }
          ],
          "text": "Lung volume reduction surgery (procedure)"
        },
        "subject": {
          "reference": "Patient/5a7dc54cf2f5f10100361927"
        },
        "context": {
          "reference": "Encounter/8b4b0a06-61bf-41e1-8aab-3acf5b6bc750"
        },
        "performedPeriod": {
          "start": "1988-10-04T03:07:26+00:00",
          "end": "1988-10-04T03:22:26+00:00"
        },
        "reasonReference": [
          {
            "reference": "Condition/7d5620a5-6a07-46d5-957d-97043c153bba",
            "display": "Chronic obstructive bronchitis (disorder)"
          }
        ]
      }
    """,
    "Condition": """{
        "resourceType": "Condition",
        "id": "7d5620a5-6a07-46d5-957d-97043c153bba",
        "clinicalStatus": "active",
        "verificationStatus": "confirmed",
        "code": {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "185086009",
              "display": "Chronic obstructive bronchitis (disorder)"
            }
          ],
          "text": "Chronic obstructive bronchitis (disorder)"
        },
        "subject": {
          "reference": "Patient/5a7dc54cf2f5f10100361927"
        },
        "context": {
          "reference": "Encounter/8b4b0a06-61bf-41e1-8aab-3acf5b6bc750"
        },
        "onsetDateTime": "1965-09-21T03:07:26+00:00",
        "assertedDate": "1965-09-21T03:07:26+00:00"
      }""",
    "DiagnosticReport": """{
        "resourceType": "DiagnosticReport",
        "id": "a3235758-d9d7-4180-8d25-a4b234bac9d2",
        "status": "final",
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "51990-0",
              "display": "Basic Metabolic Panel"
            }
          ],
          "text": "Basic Metabolic Panel"
        },
        "subject": {
          "reference": "Patient/5a7dc54cf2f5f10100361927"
        },
        "context": {
          "reference": "Encounter/1e0a380b-b5cb-4cef-9a64-d2a475fbdcb6"
        },
        "effectiveDateTime": "1986-07-29T03:07:26+00:00",
        "issued": "1986-07-29T03:07:26.398+00:00",
        "result": [
          {
            "reference": "Observation/fdaa6b7b-46ca-4618-be51-4979a58c1fd4",
            "display": "Hemoglobin A1c/Hemoglobin.total in Blood"
          },
          {
            "reference": "Observation/a30c0603-3d83-4cc9-a176-f28151ba0095",
            "display": "Glucose"
          },
          {
            "reference": "Observation/0d3604e0-f7f3-4f54-b739-c106fa069fc9",
            "display": "Urea Nitrogen"
          },
          {
            "reference": "Observation/3a8348aa-e0bb-4b1a-ac30-e09ae8465de5",
            "display": "Creatinine"
          },
          {
            "reference": "Observation/c324eb28-c18e-4ed1-9349-8c5105c4d6dc",
            "display": "Calcium"
          },
          {
            "reference": "Observation/7c88753e-3a35-40e8-8084-61f4217cfda8",
            "display": "Sodium"
          },
          {
            "reference": "Observation/b72073ea-a588-4c2f-b8ab-cf0794eaa1be",
            "display": "Potassium"
          },
          {
            "reference": "Observation/752570a5-76ae-4045-b8ae-8f96635037e1",
            "display": "Chloride"
          }
        ]
      }"""
}