import { Injectable, inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { map, take } from 'rxjs/operators';

export const RoleGuard: CanActivateFn = (route, state) => {
  const router = inject(Router);
  const user$ = inject(AuthService).user$;

  return user$.pipe(
    take(1),
    map(user => {
      const roles = user?.roles || [];

      if (roles.includes('ADMIN') || roles.includes('SUPER_USER')) {
        return true;
      }
      router.navigate(['/home']);
      return false;
    })
  );
};
