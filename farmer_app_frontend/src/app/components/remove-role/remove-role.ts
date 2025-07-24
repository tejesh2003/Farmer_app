import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { RoleService } from '../../services/role.service';

@Component({
  selector: 'app-remove-role',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './remove-role.html',
  styleUrl: './remove-role.css'
})
export class RemoveRole {
  roleForm: FormGroup;
  success = false;

  constructor(private fb: FormBuilder, private roleService: RoleService) {
    this.roleForm = this.fb.group({
      user_name: ['', Validators.required],
      role: ['ADMIN', Validators.required]
    });
  }

  submit(): void {
    if (this.roleForm.invalid) return;

    this.roleService.removeRole(this.roleForm.value).subscribe({
      next: () => {
        this.success = true;
        this.roleForm.reset({ role: 'ADMIN' });
      },
      error: err => console.error('Failed to remove role:', err)
    });
  }
}
