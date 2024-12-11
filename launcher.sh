
#!/bin/bash

echo "-----------------------------------------------------------------------------"
echo "|                   © Execution Policy Bot for 421 game                     |"
echo "| Author : Alexis EGEA                                                      |"
echo "-----------------------------------------------------------------------------"
echo

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	PYTHON_CMD=python3
elif [[ "$OSTYPE" == "cygwin"* || "$OSTYPE" == "msys"* ]]; then
 	PYTHON_CMD=python
else
	echo "Unsupported OS '$OSTYPE'"
	exit 1
fi

cd src/

while true; do
    echo "For this project, you have 3 possibilities:"
    echo "  1. Play a game of 421"
    echo "  2. Play a random bot"
    echo "  3. Play policy-based bot"
    read -p $"Select a number: " user_choice
    
    case "$user_choice" in
        1)
            echo "You chose to play a game of 421 (human)."
            echo
            $PYTHON_CMD -m launcher_humane
            break
            ;;
        2)
            echo "You chose to play the random bot."
            $PYTHON_CMD -m launcher_random
            break
            ;;
        3)
            echo "You chose to play the policy-based bot."
            $PYTHON_CMD -m launcher_policy
            break
            ;;
        *)
            echo "Invalid choice. Please select 1, 2, or 3."
            ;;
    esac
done


cd ..

echo 
read -p "Press any key to close the terminal window"
