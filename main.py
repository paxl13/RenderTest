import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Configure Flask to serve React build files
app = Flask(__name__, 
            static_folder='frontend/build/static',
            template_folder='frontend/build')
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

# Initialize Supabase client
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_KEY must be set in environment variables"
    )

supabase: Client = create_client(supabase_url, supabase_key)


# Serve React app for non-API routes
@app.route("/")
@app.route("/<path:path>")
def serve_react(path=""):
    # Don't serve React for API routes
    if path.startswith('api/'):
        return {"error": "API route not found"}, 404
    return render_template("index.html")


@app.route("/api/contacts", methods=["POST"])
def create_contact():
    try:
        data = request.get_json()
        
        # Insert data into Supabase
        result = (
            supabase.table("mytable")
            .insert(
                {
                    "name": data.get("name"),
                    "email": data.get("email"),
                    "phone": data.get("phone"),
                    "compagny": data.get("company"),  # Note: using 'compagny' to match schema
                    "notes": data.get("notes"),
                }
            )
            .execute()
        )

        if result.data:
            return jsonify({"success": True, "data": result.data})
        else:
            return jsonify({"error": "Failed to save data"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/health")
def health():
    return {"status": "healthy", "message": "App is running"}


@app.route("/api/contacts")
def get_contacts():
    try:
        result = supabase.table("mytable").select("*").execute()
        return result.data
    except Exception as e:
        return {"error": str(e)}, 500


@app.route("/api/contacts/<int:contact_id>", methods=["PUT"])
def update_contact(contact_id):
    try:
        data = request.get_json()
        
        # Update data in Supabase
        result = (
            supabase.table("mytable")
            .update(
                {
                    "name": data.get("name"),
                    "email": data.get("email"),
                    "phone": data.get("phone"),
                    "compagny": data.get("company"),  # Note: using 'compagny' to match schema
                    "notes": data.get("notes"),
                }
            )
            .eq("id", contact_id)
            .execute()
        )

        if result.data:
            return jsonify({"success": True, "data": result.data})
        else:
            return jsonify({"error": "Contact not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/contacts/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    try:
        # Delete data from Supabase
        result = (
            supabase.table("mytable")
            .delete()
            .eq("id", contact_id)
            .execute()
        )

        if result.data:
            return jsonify({"success": True, "message": "Contact deleted"})
        else:
            return jsonify({"error": "Contact not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
