#!/usr/bin/env python3
"""
Build script for React frontend
"""
import os
import subprocess
import shutil

def build_frontend():
    """Build the React frontend and prepare for Flask serving."""
    print("Building React frontend...")
    
    # Change to frontend directory
    os.chdir('frontend')
    
    # Install dependencies if node_modules doesn't exist
    if not os.path.exists('node_modules'):
        print("Installing pnpm dependencies...")
        subprocess.run(['pnpm', 'install'], check=True)
    
    # Build React app with Vite
    print("Building React app...")
    subprocess.run(['pnpm', 'run', 'build'], check=True)
    
    # Go back to root directory
    os.chdir('..')
    
    print("✅ Frontend build complete!")
    print("📁 Build files are in frontend/build/")
    print("🚀 Flask will serve React from /")

if __name__ == "__main__":
    build_frontend()