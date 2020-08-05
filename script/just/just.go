package main

import (
	"fmt"
	"os"
	"os/exec"
	"strings"

	"github.com/kardianos/osext"
)

func main() {
	selfExecutablePath, err := osext.Executable()
	directory, err := osext.ExecutableFolder()

	if err != nil {
		panic("Could not determine the current directory")
	}

	fmt.Printf("Running in: %s\n", directory)

	hasJustBeenBuilt := false ||
		strings.HasSuffix(selfExecutablePath, "\\script\\just\\just.exe") ||
		strings.HasSuffix(selfExecutablePath, "/script/just/just")

	if len(os.Args) == 1 && hasJustBeenBuilt {
		err := moveSelfUp(selfExecutablePath)

		if err != nil {
			fmt.Fprintln(os.Stderr, "Failed to move executable up")
			os.Exit(4)
		}
		fmt.Println("Sucessfully moved self up two directories")
		os.Exit(0)
	}

	// error, missing argument name
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "Error, missing command name\n\n"+
			"Syntax:  ./just <command-name> [<command-arg>...]")
		os.Exit(1)
	}

	prefixArgSlice, err := getPrefixArgSlice(os.Args[1])

	if err != nil {
		fmt.Fprintln(os.Stderr, err.Error())
		os.Exit(1)
	}

	targetExecPath, err := exec.LookPath(prefixArgSlice[0])

	if err != nil {
		fmt.Fprintln(os.Stderr, err.Error())
		os.Exit(2)
	}

	cmd := exec.Cmd{
		Path:   targetExecPath,
		Args:   append(prefixArgSlice, os.Args[2:]...),
		Dir:    directory,
		Stdin:  os.Stdin,
		Stdout: os.Stdout,
		Stderr: os.Stderr,
	}

	fmt.Printf("Running command: %s\n", cmd.String())

	err = cmd.Run()

	if err != nil {
		fmt.Fprintln(os.Stderr, err.Error())
		os.Exit(8)
	}
}

func moveSelfUp(executable string) error {
	replacer := strings.NewReplacer(
		"\\script\\just\\", "\\",
		"/script/just/", "/",
	)

	err := os.Rename(executable, replacer.Replace(executable))
	return err
}

func getPrefixArgSlice(commandName string) ([]string, error) {
	empty := []string{}
	poetry := append(empty, "poetry")
	python := append(poetry, "run", "python")
	manage := append(python, "web_server/manage.py")

	scope := empty

	switch commandName {
	case "poetry":
		scope = empty
	case "python":
		scope = poetry
	case "manage":
		return manage, nil
	case "migrate", "makemigrations", "runserver", "startapp":
		scope = manage
	default:
		return nil, fmt.Errorf("Unknow command name: %s", commandName)
	}

	return append(scope, commandName), nil
}
