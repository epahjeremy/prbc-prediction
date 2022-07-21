# prbc-predict

The transfusion of packed red blood cells (pRBCs) saves lives, but	  iron overload limits the
survival  of chronically  transfused patients.  Quality  control  destroying  pRBCs  reveals  that
hemoglobin (38.5 - 79.9 g) and heme iron (	133.42  –  276.89 mg)	 vary substantially between
pRBCs.  Yet , neither hemoglobin nor iron content can be quantified for individual clinically
used pRBCs leading to rules of thumb for pRBC transfusions.
Keeping their integrity, we sought to predict hemoglobin/iron content of any given pRBC unit
applying eight machine learning models on 6,058 pRBCs. Based on thirteen features routinely
collected  during  blood  donation,  production   and  quality  control   testing,	  we   identified   the
model with best trade-off between performance and complexity in hemoglobin/iron content
prediction.	 Validation of this model 	in an independent cohort of 2,637 pRBCs confirmed an
adjusted   R	2   >   0.9   for	  prediction   of  	individual   hemoglobin/iron   content   of   pRBCs
corresponding   to     a   mean   absolute   prediction   error  of   ≤1.43  g   hemoglobin/4.96   mg   iron
(associated   standard   deviation:   ≤1.13   g   hemoglobin/3.92   mg   iron).  	Such   unprecedented
precise   prediction   enables   reliable   pRBC   dosing   per   pharmaceutically   active   agent,   and
monitoring   iron   uptake   in   patients   and   individual   iron   loss   in   donors.   The   model   was
implemented in a free open-source web application to facilitate clinical application:


https://share.streamlit.io/epahjeremy/prbc-prediction/main/HbPrediction.py
