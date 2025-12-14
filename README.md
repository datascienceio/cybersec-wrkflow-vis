# cybersec-wrkflow-vis 

Simplified hypothetical cybersecurity workflow visualisation, implementing Kedro-Viz (for python 3.11)

1. Activate virtaul environment with Bash Terminal:

   python -m venv .venv
source .venv/Scripts/activate

2. Install dependencies:

   pip install kedro kedro-viz

3. Generate workflow:

   kedro run

4. Launch kedro-viz:

python -W "default:Kedro is not yet fully compatible" -m kedro viz run
   
