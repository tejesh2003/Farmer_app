import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RemoveRole } from './remove-role';

describe('RemoveRole', () => {
  let component: RemoveRole;
  let fixture: ComponentFixture<RemoveRole>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RemoveRole]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RemoveRole);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
