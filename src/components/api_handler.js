const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/handle_data").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])