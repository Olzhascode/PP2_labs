import json

def parse_interface_status(filename="sample-data.json"):
        
        with open(filename, 'r') as f:
            data = json.load(f)

        print("Status")
        print("=" * 85)
        print("{:<50} {:<20} {:<6} {:<6}".format("DN", "Description", "Speed", "MTU"))
        print("-" * 85)

        for interface in data["imdata"]:
            attributes = interface["l1PhysIf"]["attributes"]
            dn = attributes["dn"]
            description = attributes.get("descr", "")  
            speed = attributes.get("speed", "inherit")
            mtu = attributes.get("mtu", "9150")

            print("{:<50} {:<20} {:<6} {:<6}".format(dn, description, speed, mtu))

parse_interface_status()