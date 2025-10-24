# 🌩️ Multi-Cloud Deployment Manager with Failover Support

## 🎯 Overview
This Python mini-project demonstrates a **Multi-Cloud Deployment Manager** that automatically switches to another cloud provider in case of failure — ensuring **resilient and continuous deployment**.

It supports **SDG 9: Industry, Innovation, and Infrastructure**, focusing on building **reliable and sustainable digital infrastructure**.

---

## 🧩 Features
✅ Simulates deployment across AWS, Azure, and Google Cloud  
✅ Automatic **failover** when a cloud fails  
✅ Health monitoring and status checks  
✅ Simple Python-only implementation (no external APIs)  
✅ Extendable to real cloud SDKs

---

## ⚙️ How It Works
1. The script “deploys” an app to the first available cloud.  
2. It continuously checks each provider’s status.  
3. If the current provider goes down, it **fails over** to another.  
4. The simulation prints logs showing deployment and failover actions.

---

## 🖥️ Run the Project

### 1️⃣ Clone or Download
```bash
git clone https://github.com/your-username/MultiCloud-Deployment-Manager.git
cd MultiCloud-Deployment-Manager

### 2️⃣ Run the Script
```bash
python multi_cloud_manager.py

###you will see output like

🚀 Starting Multi-Cloud Deployment with Failover Support

✅ MyWebApp successfully deployed on AWS cloud.
🌐 Active Cloud: AWS

🩺 Health Check Cycle 1
✅ AWS cloud healthy.
🩺 Health Check Cycle 2
❌ AWS failed! Triggering failover...
✅ MyWebApp successfully deployed on Azure cloud.
🌐 Active Cloud: Azure

###📊 SDG 9 Alignment

This project supports Sustainable Development Goal 9 by:

Building resilient infrastructure

Promoting innovation in cloud systems

Ensuring continuous service availability

