function generatePin() {
    const digitCount = document.getElementById('digit-count').value;
    const repudiation = document.querySelector('input[name="repudiation"]:checked').value;
    const zero = document.querySelector('input[name="zero"]:checked').value;

    fetch('/generate_pin', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            digit_count: digitCount,
            repudiation: repudiation,
            zero: zero
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('pin-output').innerText = `Generated PIN: ${data.pin}`;
    });
}
