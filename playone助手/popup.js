document.addEventListener('DOMContentLoaded', function () {
    var checkButton = document.getElementById('checkCookies');
    checkButton.addEventListener('click', function () {
        var url = "https://www.goplayone.com/";
        var userInfo = '';

        // Check for USER_ID cookie
        chrome.cookies.get({ url: url, name: 'USER_TOKEN' }, function (cookie) {
            if (cookie) {
                userInfo += `${cookie.value}\n`; // Add USER_ID to userInfo
                // Check for USER_TOKEN cookie inside USER_ID callback to ensure order
                chrome.cookies.get({ url: url, name: 'USER_ID' }, function (cookieToken) {
                    if (cookieToken) {
                        userInfo += `${cookieToken.value}\n`; // Add USER_TOKEN to userInfo
                        // Now that we have both values, copy to clipboard
                        copyTextToClipboard(userInfo.trim());
                    } else {
                        displayCookie('USER_ID', 'Not found'); // Fallback in case USER_TOKEN not found
                    }
                });
            } else {
                displayCookie('USER_TOKEN', 'Not found'); // Fallback in case USER_ID not found
            }
        });
    }, false);
});

function displayCookie(name, value) {
    var display = document.getElementById('cookieDisplay');
    display.textContent += `${name}: ${value}\n`; // Show not found messages in UI
}

function copyTextToClipboard(text) {
    navigator.clipboard.writeText(text).then(function () {
        console.log('Async: Copying to clipboard was successful!');
    }, function (err) {
        console.error('Async: Could not copy text: ', err);
    });
}
