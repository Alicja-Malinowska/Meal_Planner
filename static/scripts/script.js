//this is taken from github (https://github.com/miguelcobain/ember-paper/issues/1058)
// missing forEach on NodeList for IE11
// this is needed to have forEach work in IE11
if (window.NodeList && !NodeList.prototype.forEach) {
  NodeList.prototype.forEach = Array.prototype.forEach;
}

$('.datepicker').pickadate({
  selectMonths: true, // Creates a dropdown to control month
  selectYears: 15, // Creates a dropdown of 15 years to control year,
  today: 'Today',
  clear: false,
  close: 'Close',
  closeOnSelect: true, // Close upon selecting a date,
  container: undefined, // ex. 'body' will append picker to body
  format: 'yyyy-mm-dd'
});

// a fix that makes datepicker stay visible
$('.datepicker').on('mousedown', function (event) {
  event.preventDefault();
})

// by setting readonly to false, 'required' on the html element works
$(".datepicker").prop('readonly', false);

// submit the form as soon as date was selected

$('#jump_to').change(function () {
  $('#date_form').submit();
});


// submit the form as soon as tag is selected 
$('#tag').change(function () {
  $('#tag-search').submit();
});


// gets the recipe id to the modal
$('.modal').modal({
  ready: function (modal, trigger) {
    modal.find('input[name="recipe_id"]').val(trigger.data('id'))
  }
});

$('select').material_select();

// a fix that ensures that when drop-down is open, it doesn't automatically hide
document.querySelectorAll('.select-wrapper').forEach(function (t) {
  t.addEventListener('click', function (e) {
    e.stopPropagation()
  })
})

$(".button-collapse").sideNav();