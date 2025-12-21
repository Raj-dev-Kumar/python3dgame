import os
import subprocess
import sys

def main():
    print("Building your Panda3D game...")
    print("=" * 40)

    # Run the build command
    result = subprocess.run(
        [sys.executable, "setup.py", "build_apps"],
        cwd=os.path.dirname(__file__)  # Run in the script's directory
    )

    if result.returncode == 0:
        print("=" * 40)
        print("Build completed successfully!")
        print("Your executable is in the 'build' folder (usually build/win_amd64/).")
    else:
        print("=" * 40)
        print("Build failed! Check the errors above.")

    input("\nPress Enter to close this window...")

if __name__ == "__main__":
    main()