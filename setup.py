import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bigfastapi",                     # This is the name of the package
    version="0.6.1",                        # This is the updated release version
    author="BigFastAPI Team",                     # Full name of the author
    author_email="support@bigfa.st",
    entry_points='''
       [console_scripts]
       cooltool=bigfastapi.scripts.main:main 
       ''',
    description="Adding lots of functionality to FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=['bigfastapi',
                                                'bigfastapi.schemas',
                                                'bigfastapi.models',
                                                'bigfastapi.db',
                                                'bigfastapi.core',
                                                'bigfastapi.services',
                                                'bigfastapi.utils',
                                                'bigfastapi.templates',
                                                'bigfastapi.scripts',
                                                'bigfastapi.scripts.commands',
                                                'bigfastapi.scripts.core',
                                                'bigfastapi.data',
                                                'migrations']),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    python_requires='>=3.8',
    install_requires=['Jinja2', 'fastapi',
                        'wheel',
                        'uvicorn',
                        'aioredis',
                        'aiosmtplib',
                        'anyio',
                        'alembic',
                        'asgiref',
                        'async-timeout',
                        'blinker',
                        'certifi',
                        'cffi',
                        'charset-normalizer',
                        'click',
                        'dnspython',
                        'email-validator',
                        'fastapi',
                        'fastapi-mail',
                        'fastapi-utils',
                        'greenlet',
                        'h11',
                        'idna',
                        'Jinja2',
                        'MarkupSafe',
                        'packaging',
                        'passlib',
                        'python-jose',
                        'pdfkit',
                        'pycparser',
                        'pydantic',
                        'fastapi_pagination',
                        'PyJWT',
                        'pyparsing',
                        'authlib',
                        'qrcode',
                        'pdfkit',
                        'python-decouple',
                        'python-dotenv',
                        'cryptography',
                        'python-jose[cryptography]',
                        'python-multipart',
                        'PyYAML',
                        'requests',
                        'rfc3986',
                        'six',
                        'sniffio',
                        'sortedcontainers',
                        'SQLAlchemy',
                        'starlette',
                        'typing-extensions',
                        'uvicorn',
                        'watchgod',
                        'websockets',
                        'validators',
                        'pytest',
                        'fastapi-pagination',
                        'qrcode',
                        'mysql-connector-python',
                        'itsdangerous'],
    url='https://bigfa.st/',
    keywords='fastapi, bigfastapi, auth',
    package_data={
#         'bigfastapi': ['templates/*.*', 'data/*.*', 'templates/email/*.html'],
#         'bigfastapi': ['templates/*.*', 'data/*.*', 'templates/landing-page/*.*'],

        'bigfastapi': ['templates/*.*', 'data/*.*', 'templates/landing-page/*.*', 'templates/email/*.*'],
    },
    # include_package_data=True,
    project_urls={
        'Bug Reports': 'https://github.com/bigfastcode/bigfastapi/issues',
        'Funding': 'https://bigfa.st/',
        'Source': 'https://github.com/bigfastcode/bigfastapi',
    },
)
