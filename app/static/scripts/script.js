var cat_ref = document.getElementById('catalogue_reference'),
    cat_ref_label = document.querySelector('label[for=catalogue_reference]'),
    references = ['ADM 1/24558', 'PROB 11', 'IND 1/17276', 'WO 13/4327'],
    span = document.createElement('span'),
    message = document.createTextNode('Try the reference shown below by submitting the form empty'),
    radios = document.querySelectorAll('input[type=radio]');

// Randomly assign a radio button
radios[(() => Math.floor(Math.random() * radios.length))()].setAttribute('checked', 'checked');

// Randomly assign a placeholder
cat_ref.setAttribute('placeholder', references[(() => Math.floor(Math.random() * references.length))()]);
cat_ref.removeAttribute('required');

// Inject the message
span.appendChild(message);
cat_ref_label.appendChild(span);

// Submit with placeholder if field is empty
document.addEventListener('submit', function(e) {
    if (!cat_ref.value) {
        cat_ref.value = cat_ref.getAttribute('placeholder');
    }
})