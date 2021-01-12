import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
   name="custom_color_palette",
   version="3.1",
   author="Joao Henry Huamán Chinchay",
   author_email="joaohenry23@gmail.com",
   description="Creates a custom color palette",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/joaohenry23/custom_color_palette",
   license='BSD 3-Clause',
   packages=setuptools.find_packages(),
   classifiers=[
      "Programming Language :: Python :: 2",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: BSD License",
      "Operating System :: OS Independent",
   ],
   python_requires='>=2.7',
   install_requires=[
      "numpy",
      "matplotlib",
   ],
)
