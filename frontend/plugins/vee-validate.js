import Vue from 'vue';
import { extend, ValidationObserver, ValidationProvider, configure } from 'vee-validate';
import { required, email, alpha_num, confirmed } from 'vee-validate/dist/rules';

Vue.component('ValidationProvider', ValidationProvider);
Vue.component('ValidationObserver', ValidationObserver);

configure({
  classes: {
    valid: 'is-valid',
    invalid: 'error'
  }
});

extend('required', {
  ...required,
  message: 'The {_field_} field is required.'
});

extend('alpha_num', {
  ...alpha_num,
  message: 'The {_field_} field accepts alphanumeric characters only.'
});

extend('min', {
  validate(value, args) {
    return value.length >= args.length;
  },
  params: ['length'],
  message: 'The {_field_} field requires a minimum of {length} characters.'
});

extend('max', {
  validate(value, args) {
    return value.length <= args.length;
  },
  params: ['length'],
  message: 'The {_field_} field must be less than {length} characters.'
});

extend('minmax', {
  validate(value, { min, max }) {
    return value.length >= min && value.length <= max;
  },
  params: ['min', 'max'],
  message: 'The {_field_} field must be between {min} and {max} characters.'
});

extend('email', {
  ...email,
  message: 'A valid email is required.'
});

extend('confirmed', {
  ...confirmed,
  message: 'The {_field_} does not match.'
});
