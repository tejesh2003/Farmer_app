import { ChangeDetectorRef, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { RoleService } from '../../services/role.service';

@Component({
  selector: 'app-add-role',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './add-role.html',
  styleUrl: './add-role.css'
})
export class AddRole {
  roleForm: FormGroup;
  success = false;

  constructor(private fb: FormBuilder, private roleService: RoleService, private cdr: ChangeDetectorRef) {
    this.roleForm = this.fb.group({
      user_name: ['', Validators.required],
      role: ['ADMIN', Validators.required]
    });
  }

  submit(): void {
    if (this.roleForm.invalid) return;

    this.roleService.addRole(this.roleForm.value).subscribe({
      next: () => {
        this.success = true;
        this.roleForm.reset({ role: 'ADMIN' });
        this.cdr.detectChanges();
      },
      error: err => console.error('Failed to assign role:', err)
    });
  }
}
