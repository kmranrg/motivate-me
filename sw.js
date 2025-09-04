const CACHE = "motivateme-v1";
const ASSETS = [
  "/",
  "/icon.png",
  "/manifest.webmanifest"
];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.map(k => (k === CACHE ? null : caches.delete(k))))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (e) => {
  const { request } = e;
  // Network-first for the main page; cache-first for static assets
  if (request.mode === "navigate") {
    e.respondWith(
      fetch(request).catch(() => caches.match("/"))
    );
  } else {
    e.respondWith(
      caches.match(request).then(cached => cached || fetch(request))
    );
  }
});
