ROUTE_ROLE_PERMISSIONS= {
    "/add-role": ["ADMIN", "SUPER_USER"],
    "/remove-role": ["ADMIN", "SUPER_USER"],
    "/farmer": ["ADMIN", "SUPER_USER"],
    "/farm": ["ADMIN", "SUPER_USER"],
    "/schedules": ["ADMIN", "SUPER_USER"],
    "/schedules/due": ["USER", "ADMIN", "SUPER_USER"],
    "/farmers/by-crop": ["USER", "ADMIN", "SUPER_USER"],
    "/bill": ["USER", "ADMIN", "SUPER_USER"],
}