/**
 * @jest-environment jsdom
 */

document.body.innerHTML = `
    <div>
        <i id="notificationBell" data-unread-count="3"></i>
        <span id="unreadCount" class="badge bg-danger position-absolute top-0 start-100 translate-middle p-2 rounded-circle"></span>
    </div>
`;

require('./notification.js');