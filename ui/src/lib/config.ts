export interface TelamonConfig {
  basePath: string
  apiPath: string
  title: string
}

declare global {
  interface Window {
    __TELAMON__?: TelamonConfig
  }
}

const fallback: TelamonConfig = { basePath: '/admin', apiPath: '/admin/_api', title: 'Telamon Admin' }
const raw = window.__TELAMON__
export const config: TelamonConfig =
  raw && typeof raw === 'object' && 'apiPath' in raw ? raw : fallback
