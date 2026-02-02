#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dependency installer for Gemini NVDA Add-on.

This script installs the required Python packages into the add-on's lib directory
using uv (recommended) or pip as fallback.

Usage:
    python install_deps.py

Or with uv directly:
    uv pip install -r requirements.txt --target lib
"""

import os
import sys
import subprocess
import shutil

# Directory paths
ADDON_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = os.path.join(ADDON_DIR, "lib")
REQUIREMENTS_FILE = os.path.join(ADDON_DIR, "requirements.txt")

# Python version check (NVDA uses 3.11)
REQUIRED_PYTHON = (3, 11)


def check_python_version():
    """Check if Python version is compatible."""
    current = sys.version_info[:2]
    if current < REQUIRED_PYTHON:
        print(f"Warning: Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}+ recommended.")
        print(f"Current version: {current[0]}.{current[1]}")
    return True


def find_uv():
    """Find uv executable."""
    # Check if uv is in PATH
    uv_path = shutil.which("uv")
    if uv_path:
        return uv_path

    # Check common installation locations on Windows
    home = os.path.expanduser("~")
    possible_paths = [
        os.path.join(home, ".local", "bin", "uv"),
        os.path.join(home, ".local", "bin", "uv.exe"),
        os.path.join(home, ".cargo", "bin", "uv"),
        os.path.join(home, ".cargo", "bin", "uv.exe"),
        os.path.join(os.environ.get("LOCALAPPDATA", ""), "uv", "uv.exe"),
    ]

    for path in possible_paths:
        if os.path.exists(path):
            return path

    return None


def install_with_uv(uv_path):
    """Install dependencies using uv."""
    print(f"Using uv: {uv_path}")
    print(f"Installing to: {LIB_DIR}")

    # Create lib directory
    os.makedirs(LIB_DIR, exist_ok=True)

    # Run uv pip install
    cmd = [
        uv_path,
        "pip",
        "install",
        "-r", REQUIREMENTS_FILE,
        "--target", LIB_DIR,
        "--python", f"{sys.version_info[0]}.{sys.version_info[1]}",
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=False)

    return result.returncode == 0


def install_with_pip():
    """Install dependencies using pip (fallback)."""
    print("uv not found, using pip...")
    print(f"Installing to: {LIB_DIR}")

    # Create lib directory
    os.makedirs(LIB_DIR, exist_ok=True)

    # Run pip install
    cmd = [
        sys.executable,
        "-m", "pip",
        "install",
        "-r", REQUIREMENTS_FILE,
        "--target", LIB_DIR,
        "--upgrade",
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=False)

    return result.returncode == 0


def clean_lib_dir():
    """Remove existing lib directory."""
    if os.path.exists(LIB_DIR):
        print(f"Cleaning existing lib directory: {LIB_DIR}")
        shutil.rmtree(LIB_DIR)


def main():
    print("=" * 60)
    print("Gemini NVDA Add-on - Dependency Installer")
    print("=" * 60)
    print()

    # Check Python version
    check_python_version()

    # Check requirements file exists
    if not os.path.exists(REQUIREMENTS_FILE):
        print(f"Error: requirements.txt not found at {REQUIREMENTS_FILE}")
        return 1

    # Ask about cleaning
    if os.path.exists(LIB_DIR):
        response = input("Clean existing lib directory? [y/N]: ").strip().lower()
        if response == "y":
            clean_lib_dir()

    # Try uv first
    uv_path = find_uv()
    if uv_path:
        success = install_with_uv(uv_path)
    else:
        print()
        print("Note: uv is recommended for faster installs.")
        print("Install uv: https://docs.astral.sh/uv/getting-started/installation/")
        print()
        success = install_with_pip()

    if success:
        print()
        print("=" * 60)
        print("Installation complete!")
        print("Restart NVDA to use the Gemini add-on.")
        print("=" * 60)
        return 0
    else:
        print()
        print("=" * 60)
        print("Installation failed!")
        print("Please check the error messages above.")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
