# $ docker build -t jupyterhub-tutorial:first .
# $ docker run --mount type=bind,src="/Users/austinchang/tutorials/python/jupyter/jupyterhub",dst="/srv/jupyterhub/bm" -p 8000:8000 -d --name jupyterhub jupyterhub-tutorial:first
# $ docker exec -it jupyterhub bash
FROM jupyterhub/jupyterhub
RUN pip install dockerspawner
RUN jupyterhub --generate-config
RUN sed -i "s/^#c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'$/c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'/" jupyterhub_config.py
#RUN sed -i "s/^#c.JupyterHub.hub_ip = '127.0.0.1'$/c.JupyterHub.hub_ip = '0.0.0.0'/" jupyterhub_config.py
RUN sed -i "s/^#c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'$/c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'/" jupyterhub_config.py
ENTRYPOINT ["jupyterhub", "--debug"]