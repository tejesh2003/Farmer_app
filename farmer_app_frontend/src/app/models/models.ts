export interface User{
    id: number;
    user_name: string;
    roles: string[];
}

export interface Farmer {
  id: number;
  name: string;
  phone: string;
  language: string;
  farm_ids: number[];
  country:number;
}

export interface CreateFarmer {
  name: string;
  phone: string;
  language: string;
  country: string;
}

export interface CreateFarm {
  village: string;
  sowing_date: string; 
  area: number;
  crop: string;
  farmer_id: number;
}

export interface CreateSchedule {
  fertiliser: string;
  quantity: number;
  unit: 'kg' | 'L';
  days_after_sowing: number;
  farm_id: number;
}

export interface EditRole {
  user_name: string;
  role: 'ADMIN';
}

export interface Schedule {
  days_after_sowing: number;
  due_date: string;
  farm_id: number;
  fertiliser: string;
  id: number;
  quantity: number;
  unit: string;
}

export interface FarmerBill {
  farmer_id: number;
  total_cost: number;
  fertilizers: {
    [fertiliser: string]: {
      total_quantity: number;
      unit: string;
      price_per_unit: number;
      total_cost: number;
      farms: {
        crop: string;
        farm_id: number;
        quantity: number;
        due_date: string;
      }[];
    };
  };
}

