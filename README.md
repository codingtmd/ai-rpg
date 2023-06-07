# ai-rpg

## folder structure

 - Detective: the folder to host all the sudo code for the detective game category
    - Main.sudo:  the main structure for the game, which will be used as the schema
    - Main.sudo.gen: the final generated prompt for gpt LLM
    - *.sodu: the pre-defined class-style definition of each sub-component of the game
 - sudogen.py: the script for generating the prompts


## How to use

for example, you can change the .sudo file of any class, and in the end, run below command to generate a full prompt

```
python3 sudogen.py ./Detective/Main.sudo
```

