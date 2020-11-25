$(document).ready(function(){
  $('.sidenav').sidenav();
  $('select').formSelect();
  $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      yearRange: 30,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
  })
})