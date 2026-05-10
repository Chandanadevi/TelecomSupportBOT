from flask import Flask, request, jsonify
import random
import mysql.connector

app = Flask(__name__)

# MYSQL CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hanuman@2381",
    database="telecom_bot"
)

#cursor = db.cursor()
otp_store = {}

@app.route('/webhook', methods=['POST'])
def webhook():

    req = request.get_json()

    print("FULL REQUEST:", req)

    tag = req.get("fulfillmentInfo", {}).get("tag")

    print("TAG:", tag)

    # BALANCE FLOW
    if tag == "check-balance":

        mobile = req.get("sessionInfo", {}).get("parameters", {}).get("mobile")

        if str(mobile).strip() == "1234567890":
            balance = 349
        else:
            balance = 100

        return jsonify({
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"Your current balance is {balance} rupees"
                            ]
                        }
                    }
                ]
            }
        })
    # SEND OTP FLOW
    elif tag == "send-otp":

        mobile = req.get("sessionInfo", {}).get("parameters", {}).get("mobile_number")

        otp = "123456"

        otp_store[mobile] = otp

        print("OTP STORE:", otp_store)

        return jsonify({
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"OTP sent successfully to {mobile}"
                            ]
                        }
                    }
                ]
            }
        })

    # CREATE TICKET FLOW
    elif tag == "create-ticket":

        print("CREATE TICKET FLOW RUNNING")

        ticket_id = f"TKT{random.randint(1000,9999)}"

        mobile = req.get("sessionInfo", {}).get("parameters", {}).get("mobile")

        issue = "Network Issue"

        sql = """
        INSERT INTO complaints
        (ticket_id, mobile, issue, status)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            ticket_id,
            mobile,
            issue,
            "OPEN"
        )

        cursor.execute(sql, values)
        db.commit()

        return jsonify({
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                f"Complaint created successfully. Your ticket ID is {ticket_id}"
                            ]
                        }
                    }
                ]
            }
        })
    
    # VERIFY OTP FLOW
    elif tag == "verify-otp":

        mobile = req.get("sessionInfo", {}).get("parameters", {}).get("mobile_number")

        entered_otp = str(
            req.get("sessionInfo", {}).get("parameters", {}).get("otp_code")
        )

        actual_otp = otp_store.get(mobile)

        print("ENTERED OTP:", entered_otp)
        print("ACTUAL OTP:", actual_otp)

        if entered_otp == actual_otp:

            return jsonify({
                "sessionInfo": {
                    "parameters": {
                        "authenticated": True
                    }
                },
                "fulfillment_response": {
                    "messages": [
                        {
                            "text": {
                                "text": [
                                    "OTP verification successful"
                                ]
                            }
                        }
                    ]
                }
            })

        else:

            return jsonify({
                "sessionInfo": {
                    "parameters": {
                        "authenticated": False
                    }
                },
                "fulfillment_response": {
                    "messages": [
                        {
                            "text": {
                                "text": [
                                    "Invalid OTP"
                                ]
                            }
                        }
                    ]
                }
            })

    # DEFAULT RESPONSE
    return jsonify({
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [
                            "Webhook reached but tag not matched"
                        ]
                    }
                }
            ]
        }
    })

if __name__ == "__main__":
    app.run(port=3000)