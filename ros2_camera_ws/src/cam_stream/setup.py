from setuptools import setup

package_name = 'cam_stream'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('lib/' + package_name, [package_name+'/lib/show_img.py',
                                 package_name+'/lib/cam_boton.py',
                                 package_name+'/lib/Codigo_ranas.py' ])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pu$$yBoy',
    maintainer_email='lol',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'driver_node = cam_stream.driver_node:main',
            'image_ctrl = cam_stream.image_ctrl:main',
            'realsense_node = cam_stream.realsense_node:main'
        ],
    },
)
