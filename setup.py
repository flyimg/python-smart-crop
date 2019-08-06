from setuptools import setup

setup(name='smartcrop',
      version='0.4',
      description='OpenCV smart crop',
      url='https://github.com/flyimg/python-smart-crop',
      author='Josua Gonzalez',
      author_email='jgonzalez@epixelic.com',
      include_package_data=True,
      license='MIT',
      packages=['smartcrop'],
      scripts=['bin/smartcrop'],
      zip_safe=False)
