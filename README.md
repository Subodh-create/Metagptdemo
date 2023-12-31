# Metagptdemo
This repository consist of project created by metaGPT

# MetaGPT: The Multi-Agent Framework

<p align="center">
<a href=""><img src="https://github.com/geekan/MetaGPT/blob/main/docs/resources/MetaGPT-logo.jpeg?raw=true" alt="MetaGPT logo: Enable GPT to work in software company, collaborating to tackle more complex tasks." width="150px"></a>
</p>

<p align="center">
<b>Assign different roles to GPTs to form a collaborative software entity for complex tasks.</b>
</p>




1. MetaGPT takes a **one line requirement** as input and outputs **user stories / competitive analysis / requirements / data structures / APIs / documents, etc.**
2. Internally, MetaGPT includes **product managers / architects / project managers / engineers.** It provides the entire process of a **software company along with carefully orchestrated SOPs.**
   1. `Code = SOP(Team)` is the core philosophy. We materialize SOP and apply it to teams composed of LLMs.

![A software company consists of LLM-based roles](https://github.com/geekan/MetaGPT/blob/main/docs/resources/software_company_cd.jpeg?raw=true)

<p align="center">Software Company Multi-Role Schematic (Gradually Implementing)</p>

## Examples (fully generated by GPT-4) But we generate it from gpt-3.5 

For example, if you type `python startup.py "Design a RecSys like flipboard"`, you would get many outputs, one of them is data & api design

![Jinri Toutiao Recsys Data & API Design](https://github.com/geekan/MetaGPT/blob/main/docs/resources/workspace/content_rec_sys/resources/data_api_design.png?raw=true)

It costs approximately **$0.2** (in GPT-4 API fees) to generate one example with analysis and design, and around **$2.0** for a full project.

## Installation

### Traditional Installation

```bash
# Step 1: Ensure that NPM is installed on your system. Then install mermaid-js.
npm --version
sudo npm install -g @mermaid-js/mermaid-cli

# Step 2: Ensure that Python 3.9+ is installed on your system. You can check this by using:
python --version

# Step 3: Clone the repository to your local machine, and install it.
git clone https://github.com/geekan/metagpt
cd metagpt
python setup.py install
```

**Note:**

- If already have Chrome, Chromium, or MS Edge installed, you can skip downloading Chromium by setting the environment variable
`PUPPETEER_SKIP_CHROMIUM_DOWNLOAD` to `true`.

- Some people are [having issues](https://github.com/mermaidjs/mermaid.cli/issues/15) installing this tool globally. Installing it locally is an alternative solution,

    ```bash
    npm install @mermaid-js/mermaid-cli
    ```

- don't forget to the configuration for mmdc in config.yml

    ```yml
    PUPPETEER_CONFIG: "./config/puppeteer-config.json"
    MMDC: "./node_modules/.bin/mmdc"
    ```

- if `python setup.py install` fails with error `[Errno 13] Permission denied: '/usr/local/lib/python3.11/dist-packages/test-easy-install-13129.write-test'`, try instead running `python setup.py install --user`

### Installation by Docker

```bash
# Step 1: Download metagpt official image and prepare config.yaml
docker pull metagpt/metagpt:v0.3.1
mkdir -p /opt/metagpt/{config,workspace}
docker run --rm metagpt/metagpt:v0.3.1 cat /app/metagpt/config/config.yaml > /opt/metagpt/config/key.yaml
vim /opt/metagpt/config/key.yaml # Change the config

# Step 2: Run metagpt demo with container
docker run --rm \
    --privileged \
    -v /opt/metagpt/config/key.yaml:/app/metagpt/config/key.yaml \
    -v /opt/metagpt/workspace:/app/metagpt/workspace \
    metagpt/metagpt:v0.3.1 \
    python startup.py "Write a cli snake game"

# We can also start a container and execute commands in it
docker run --name metagpt -d \
    --privileged \
    -v /opt/metagpt/config/key.yaml:/app/metagpt/config/key.yaml \
    -v /opt/metagpt/workspace:/app/metagpt/workspace \
    metagpt/metagpt:v0.3.1

docker exec -it metagpt /bin/bash
$ python startup.py "Write a cli snake game"
```

The command `docker run ...` do the following things:

- Run in privileged mode to have permission to run the browser
- Map host directory `/opt/metagpt/config` to container directory `/app/metagpt/config`
- Map host directory `/opt/metagpt/workspace` to container directory `/app/metagpt/workspace`
- Execute the demo command `python startup.py "Write a cli snake game"`

### Build image by yourself

```bash
# We can also build metagpt image by ourself.
git clone https://github.com/geekan/MetaGPT.git
cd MetaGPT && docker build -t metagpt:custom .
```

## Configuration

- Configure  `OPENAI_API_KEY` in any of `config/key.yaml / config/config.yaml / env`
- Priority order: `config/key.yaml > config/config.yaml > env`

```bash
# Copy the configuration file and make the necessary modifications.
cp config/config.yaml config/key.yaml
```
Use model gpt-3.5-turbo-16k
![image](uploads/fa7dd82924d9baeaaf4381daa5a57817/image.png)

Uncomment this in config/key.yaml as shown in figure
![image](uploads/2faa03b02e75ba0028061cf7296c6eec/image.png)

| Variable Name                              | config/key.yaml                           | env                                             |
| ------------------------------------------ | ----------------------------------------- | ----------------------------------------------- |
| OPENAI_API_KEY # Replace with your own key | OPENAI_API_KEY: "sk-..."                  | export OPENAI_API_KEY="sk-..."                  |
| OPENAI_API_BASE # Optional                 | OPENAI_API_BASE: "https://<YOUR_SITE>/v1" | export OPENAI_API_BASE="https://<YOUR_SITE>/v1" |

## Tutorial: Initiating a startup

```shell
python startup.py "Write a cli snake game"
# Use code review will cost more money, but will opt for better code quality.
python startup.py "Write a cli snake game" --code_review True 
```

After running the script, you can find your new project in the `workspace/` directory.
### Preference of Platform or Tool 

You can tell which platform or tool you want to use when stating your requirements.
```shell
python startup.py "Write a cli snake game based on pygame"
```
### Usage

```
NAME
    startup.py - We are a software startup comprised of AI. By investing in us, you are empowering a future filled with limitless possibilities.

SYNOPSIS
    startup.py IDEA <flags>

DESCRIPTION
    We are a software startup comprised of AI. By investing in us, you are empowering a future filled with limitless possibilities.

POSITIONAL ARGUMENTS
    IDEA
        Type: str
        Your innovative idea, such as "Creating a snake game."

FLAGS
    --investment=INVESTMENT
        Type: float
        Default: 3.0
        As an investor, you have the opportunity to contribute a certain dollar amount to this AI company.
    --n_round=N_ROUND
        Type: int
        Default: 5

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```

We can check `examples` for more details on single role (with knowledge base) and LLM only examples.

## QuickStart
It is difficult to install and configure the local environment for some users. The following tutorials will allow you to quickly experience the charm of MetaGPT.  

- [MetaGPT quickstart](https://deepwisdom.feishu.cn/wiki/CyY9wdJc4iNqArku3Lncl4v8n2b)


## Index
![](https://gitlab.01cloud.com/sagar.shrestha2/mlops/uploads/c31a597b94a2df41400d414b731f7511/image.png)

![](https://gitlab.01cloud.com/sagar.shrestha2/mlops/uploads/eca601404ae3a4fefb5f1338e7e8b8f8/image.png)

![](https://gitlab.01cloud.com/sagar.shrestha2/mlops/uploads/dca4220da82cc0a682598e2d5f20e9fb/image.png)

![](https://gitlab.01cloud.com/sagar.shrestha2/mlops/uploads/98eea43eda992dc6e73735d97a6e9fd3/image.png)

![](https://gitlab.01cloud.com/sagar.shrestha2/mlops/uploads/2ec1b9e33e75bc86034fcf4d1d837f93/image.png)

![](https://gitlab.01cloud.com/sagar.shrestha2/mlops/uploads/16a027cf613336cde511c2962cdf5a50/image.png)

![](https://gitlab.01cloud.com/sagar.shrestha2/mlops/uploads/db72d355bc0393c34637f0ba01ac32b3/image.png)


## Demo

https://github.com/geekan/MetaGPT/assets/2707039/5e8c1062-8c35-440f-bb20-2b0320f8d27d
