$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.modal').modal();
  $('select').formSelect();
  $('.tooltipped').tooltip();
  $('.datepicker').datepicker({
      format: "yyyy",
      yearRange: 120,
      maxDate: new Date(2025,7,14),
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
  })
})

