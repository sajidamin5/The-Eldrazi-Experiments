import asyncio
import random
from pprint import pprint

'''
Citations (Platform, Model)

(Ollama, gemma3:1b)
🦴 Code Skellies 🦴
- ActionPotentialModel class
- update_neurotransmitter func
- run func

(OpenAI, )

(DeepSeek, )

Glycosilation: Process of adding a carbohydrate to some other group (i.e. hydroxil, amino, lipid, etc.)
- some proteins do not fold correctly unless they are glycosylated (PMID, 20301239)
'''

class ActionPotentialModel:
    def __init__(self, membrane="", ion="", threshold="", ligand="", enzyme="", 
                 catalyst="", inhibitor="", presynaptic_neuron="", postsynaptic_neuron=""):
        
        # Presets for components of an Action Potential Cascade for general model creation
        
        membranes = ["alpha-helix", "beta-helix", "beta-sheet", 
                     "(??)sigma-helix(??)", "(??)omega-helix(??)"]
        
        ions = ['Na+', 'K+','Ca2+']
        
        # (Ollama, gemma3:1b)
        # transcribing to text to data structure
        ligands = {
            "Protein Ligands" : ["G protein-coupled", "tyrosine", "transmembrane, structural"],
            "Neurotransmitters" : ["Dopamine", "Seratonin", "Norepinephrine", "Acetylcholine"],
            "Hormones" : ["Estrogen, Testosterone, Insulin, Growth Hormone (Pituitary), Cortisol, Thyroxine"],
            "Pharmaceuticals" : ["SSRIs", "Beta-blockers", "Statins", "opiods, antidepressants, analgesics, anticancerous"],
            "Amino Acids" : ["Glycine, Histidine", "Glutamate", "Aspartate", "Glycine", "Gamma-Aminobutyric (GABA)"],
            "Small Organic Molecules" : ["flavonoids, steroids, peptides, Glucose", "Adenosine Triphosphate", "NADH/NAD+"],
            "Ion Ligands" : ["Potassium", "Sodium", "Calcium", "Magnesium"],
            "Toxins" : ["Strychnine, Tetrodotoxin, Amanitin, Curare"],
            "Plant/Microbe By-product" : ["Morphine, Quinine, Cyclosporine, Digoxin"],
            "Fragrances" : ["Menthol", "Capsaicin", "Geosmin"],
            "RC/Synthetics" : ["Isoproterenol", "Forskolin", "Fluorescent Tracers"]
        } 
        
        enzymes = ["Tyrosine Kinase, Phosphodiesterase", "Phopholipases", "Signal Transducing Kinases", "Proteases"]

        catalysts = {
            "Homogenous" : ['Sulfuric Acid', 'Palladium'],
            "Heterogeneous" : ['Palladium/Carbon', 'Raney Nickel', 'Platinum', 'Rhodium on Alumina', 'Zeolites'],
            "Lewis Acid" : ['Alumnum Chloride, Boron Trifluoride', 'Ferric Chloride', 'Titanium Tetrachloride', 'Zinc Chloride'],
            "Radical" : ['Azobisisobutyronitrile', 'Benzoyl Peroxide', 'Di-tert-butyl Peroxide', 'Fenton\'s Reagent', 'Persulfate Salts']
        }
        
        inhibitors = ['cAMP', 'Calcium', 'Magnesium Ions', 'ATP', 'Lipid Hydrolases', 'Phospholipase A2', 'Lipid Phosphodiesterases', 'Proteasome Inhibitors']
        
    
        # Initialization step for each component of the Action Potential Cascade
        # TODO: work out random choice for dictionary structures
        
        if membrane is not None : self.membrane = membrane
        if ion is not None : self.ion = ion
        if threshold is not None : self.threshold = threshold
        if catalyst is not None : self.catalyst = catalyst
        if inhibitors is not None : self.inhibitor = inhibitor
        if ligands is not None: self.ligand = ligand
        if enzyme is not None : self.enzyme = enzyme
        
        self.membrane = random.choice(membranes)
        self.ion = random.choice(ions)
        self.threshold = random.randint(-70, -55)
        self.catalyst = random.choice(random.choice(list(catalysts.values())))
        self.inhibitor = random.choice(inhibitors)
        self.ligand = random.choice(random.choice(list(ligands.values())))
        self.enzyme = random.choice(enzymes)
        
        self.initial_membrane_condition = {"Membrane" : self.membrane, 
                                           "Ion" : self.ion, 
                                           "Threshold" : self.threshold, 
                                           "Catalyst" : self.catalyst, 
                                           "Inhibitor" : self.inhibitor, 
                                           "Ligand" : self.ligand, 
                                           "Enzyme" : self.enzyme}
        
        # need some function to determine adequate pre/post based on initial conditions.
        # i.e. calculate the resultant off of initial conditons [membrane, ion, threshold, catalyst, inhib ,ligand, enzyme]
        self.presynaptic_neuron = ""
        self.postsynaptic_neuron = ""
        self.resultant_neurotransmitter = "" 

    def display_initial_conditions(self):
        return pprint(self.initial_membrane_condition)
    
    def update_neurotransmitter(self, ligand_concentration):
        """
        Simulates the response of the neuron to a ligand.  This is a placeholder.
        """
        # In a real model, this would involve complex calculations.
        # For this example, we just return a simple value.
        return ligand_concentration  # Placeholder - replace with actual calculations


    async def run(self, ctx):
        """
        Runs the action potential model.  Handles the command, input data, and output.
        """

        if self.membrane == "" or self.ion == "":  # Basic validation

            await ctx.send("requires atleast a membrane and or ion")

        resultant_neurotransmitter = self.update_neurotransmitter(self.ion)  # Initial update

        # Simulate the action potential (a very simplified example)
        if self.threshold > 0:
            resultant_neurotransmitter += "Threshold reached!"

        # Add more complex logic here, like:
        #   -  Calculate the spike potential
        #   -  Model ion channel dynamics
        #   -  Include inhibitory/excitatory influences

        await ctx.send(f"Action potential triggered: {resultant_neurotransmitter}")  # Send the result



async def main():
    #Example usage:
    ap_model = ActionPotentialModel()
    return ap_model.display_initial_conditions()

if __name__ == "__main__":
    asyncio.run(main())
