import subprocess as sp

print("""
    wait for until the process complete
""")

# checking git is available or not
def gitAvailablity():
    try:
        result = sp.run(['git', '--version'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except FileNotFoundError:
        return "git is not installed"
    except sp.CalledProcessError as e:
        return f"An error occurred: {e}"

print(gitAvailablity())

def getComfyUI():
    sp.run("git clone https://github.com/comfyanonymous/ComfyUI.git && cd ComfyUI/custom_nodes",shell=True)
    sp.run("git clone https://github.com/ltdrdata/ComfyUI-Manager.git ComfyUI/custom_nodes/ComfyUI-Manager",shell=True)

getComfyUI()

def getting_huggingfacemodel():
    model_type = input("""
        hugging face checkpoint link
    """)
    sp.run(f"git clone {model_type} ComfyUI/models/checkpoints",shell=True)
    vae_type = input("""
        hugging face vae link
    """)
    sp.run(f"git clone {vae_type} ComfyUI/models/vae",shell=True)

getting_huggingfacemodel()

#developed by GT