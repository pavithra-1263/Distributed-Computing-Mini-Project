import random
import time

class CloudProvider:
    def __init__(self, name):
        self.name = name
        self.is_active = True

    def deploy_app(self, app_name):
        if not self.is_active:
            raise Exception(f"{self.name} is down!")
        print(f"✅ {app_name} successfully deployed on {self.name} cloud.")

    def check_health(self):
        self.is_active = random.choice([True, True, True, False])
        return self.is_active


class MultiCloudManager:
    def __init__(self, providers):
        self.providers = providers
        self.active_provider = None

    def deploy_with_failover(self, app_name):
        for provider in self.providers:
            provider.check_health()
            if provider.is_active:
                self.active_provider = provider
                try:
                    provider.deploy_app(app_name)
                    print(f"🌐 Active Cloud: {provider.name}\n")
                    return
                except Exception as e:
                    print(f"⚠️ Error: {e}")
            else:
                print(f"❌ {provider.name} is currently unavailable.")
        print("🚨 All providers failed! Deployment aborted.\n")

    def monitor(self):
        if self.active_provider:
            self.active_provider.check_health()
            if not self.active_provider.is_active:
                print(f"❌ {self.active_provider.name} failed! Triggering failover...\n")
                self.deploy_with_failover("MyWebApp")


if __name__ == "__main__":
    aws = CloudProvider("AWS")
    azure = CloudProvider("Azure")
    gcp = CloudProvider("Google Cloud")

    manager = MultiCloudManager([aws, azure, gcp])

    print("🚀 Starting Multi-Cloud Deployment with Failover Support\n")

    manager.deploy_with_failover("MyWebApp")

    for i in range(5):
        time.sleep(2)
        print(f"🩺 Health Check Cycle {i+1}")
        manager.monitor()
 
