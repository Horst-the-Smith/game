import pusher

pusher_client = pusher.Pusher(
  app_id='',
  key='',
  secret='',
  cluster='',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})