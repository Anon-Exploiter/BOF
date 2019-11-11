#!/usr/bin/python3

from sys import argv

def getInputVariables(varsList):
        vars    = varsList.split("\n")

        for _vars in vars:
                """
                Uncomment the below line if you think we don't need to sent \r after out input buffer
                """

                # spikeTemplate = f's_readline();\ns_string("{_vars} ");\ns_string_variable("0");\n'
                spikeTemplate = f's_readline();\ns_string("{_vars} ");\ns_string_variable("0");\ns_string("\\r\\n");\n'
                print("-----------------------")
                print(spikeTemplate)
                print("-----------------------\n")

                fileName        = f"{argv[1]}_{_vars}.spk"

                with open(fileName, 'w+') as f:
                        f.write(spikeTemplate)
                        print(f"[#] Spike Tempalte written in: {fileName}")

def main():
        varFile         = argv[1]
        with open(varFile, 'r') as f:
                getInputVariables(f.read().strip())

if __name__ == '__main__':
        main()
