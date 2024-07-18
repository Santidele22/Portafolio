import express from 'express'
import morgan from 'morgan'
import corsMiddleware from './middlewares/corsMiddlewares'
const port = 3000
const app = express()

app.use(corsMiddleware)
app.use(morgan('dev'))
app.use(express.json())
app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
