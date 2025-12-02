def vehicle_details(vehicle_no, owner_name, vehicle_type, year_of_manufacture):
    return (
        f"vehicle_no: {vehicle_no}\n"
        f"owner_name: {owner_name}\n"
        f"vehicle_type: {vehicle_type}\n"
        f"year_of_manufacture: {year_of_manufacture}\n"
    )

    return result
if __name__=="__main__":
  vehicle_no="KA25P3505"
  owner_name="priya"
  vehicle_type="car"
  year_of_manufacture="2008"  
  print(vehicle_details(vehicle_no,owner_name,vehicle_type,year_of_manufacture))
