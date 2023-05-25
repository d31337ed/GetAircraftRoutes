$('.airline-selector').select2({
    ajax: {
    url: '/airlines',
    dataType: 'json'
    }
});