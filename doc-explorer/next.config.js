/** @type {import('next').NextConfig} */
const nextConfig = {
  rewrites: async () => {
    return [
      {
        source: "/api/:path*",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://0.0.0.0:8000/api/:path*"
            : "http://0.0.0.0:8000/api/:path*",
      },
    ];
  },
  experimental: {
    proxyTimeout: 600_000,
  }
};

module.exports = nextConfig;
