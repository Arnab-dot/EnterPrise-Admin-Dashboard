"""
Connection Diagnostic Script
Run this to check Django server and CORS configuration
"""

import requests
import json

API_BASE_URL = "http://localhost:8000/api"

print("=" * 70)
print("DJANGO API CONNECTION DIAGNOSTIC")
print("=" * 70)

# Test 1: Check if server is running
print("\n1️⃣ Testing server connection...")
try:
    response = requests.get("http://localhost:8000/", timeout=5)
    print(f"   ✅ Django server is running (Status: {response.status_code})")
except requests.exceptions.ConnectionError:
    print("   ❌ Django server is NOT running!")
    print("   Start it with: python manage.py runserver")
    exit(1)
except Exception as e:
    print(f"   ❌ Error: {str(e)}")
    exit(1)

# Test 2: Test authentication endpoint
print("\n2️⃣ Testing authentication endpoint...")
try:
    response = requests.post(
        f"{API_BASE_URL}/users/token/",
        json={"email": "test@test.com", "password": "wrong"},
        timeout=5
    )
    print(f"   ✅ Auth endpoint accessible (Status: {response.status_code})")
    if response.status_code == 401:
        print("   ✅ Endpoint is working (wrong credentials expected)")
except Exception as e:
    print(f"   ❌ Auth endpoint error: {str(e)}")

# Test 3: Get valid credentials and test full flow
print("\n3️⃣ Testing with your credentials...")
email = input("   Enter your email: ")
password = input("   Enter your password: ")

try:
    response = requests.post(
        f"{API_BASE_URL}/users/token/",
        json={"email": email, "password": password},
        timeout=5
    )

    if response.status_code == 200:
        print("   ✅ Login successful!")
        data = response.json()
        token = data['access']
        print(f"   Token: {token[:30]}...")

        # Test 4: Test client endpoint with token
        print("\n4️⃣ Testing client list endpoint...")
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        response = requests.get(
            f"{API_BASE_URL}/clients/",
            headers=headers,
            timeout=5
        )

        if response.status_code == 200:
            print(f"   ✅ Client list endpoint working!")
            data = response.json()
            clients = data.get('results', data) if isinstance(data, dict) else data
            print(f"   Found {len(clients)} existing clients")
        else:
            print(f"   ❌ Client list failed: {response.status_code}")
            print(f"   Response: {response.text[:200]}")

        # Test 5: Test client creation
        print("\n5️⃣ Testing client creation...")
        test_client = {
            "username": "Diagnostic Test Client",
            "user_address": "123 Test Street",
            "dob": "1990-01-15",
            "phone_no": 9876543210
        }

        print(f"   Sending: {json.dumps(test_client, indent=2)}")

        response = requests.post(
            f"{API_BASE_URL}/clients/",
            json=test_client,
            headers=headers,
            timeout=5
        )

        print(f"   Status Code: {response.status_code}")
        print(f"   Response Headers: {dict(response.headers)}")
        print(f"   Response Body: {response.text[:500]}")

        if response.status_code == 201:
            print("   ✅ Client creation SUCCESSFUL!")
            created_client = response.json()
            print(f"   Created client ID: {created_client.get('id')}")
            print(f"   Full response: {json.dumps(created_client, indent=2)}")
        else:
            print(f"   ❌ Client creation FAILED!")
            try:
                error = response.json()
                print(f"   Error details: {json.dumps(error, indent=2)}")
            except:
                print(f"   Raw response: {response.text}")

        # Test 6: Check CORS headers
        print("\n6️⃣ Checking CORS headers...")
        if 'Access-Control-Allow-Origin' in response.headers:
            print(f"   ✅ CORS enabled: {response.headers['Access-Control-Allow-Origin']}")
        else:
            print("   ⚠️ CORS headers not found")
            print("   This might cause issues with Streamlit")
            print("   Make sure django-cors-headers is installed and configured")

    else:
        print(f"   ❌ Login failed: {response.status_code}")
        print(f"   Response: {response.text}")

except Exception as e:
    print(f"   ❌ Error: {str(e)}")
    import traceback

    traceback.print_exc()

# Summary
print("\n" + "=" * 70)
print("DIAGNOSTIC COMPLETE")
print("=" * 70)

print("\n📋 Checklist:")
print("   □ Django server running")
print("   □ Can login and get token")
print("   □ Can access client list")
print("   □ Can create client")
print("   □ CORS headers present")

print("\n💡 If any test failed, check:")
print("   1. Django server is running: python manage.py runserver")
print("   2. All migrations applied: python manage.py migrate")
print("   3. CORS installed: pip install django-cors-headers")
print("   4. settings.py has correct CORS configuration")
print("   5. User exists and has correct organization")