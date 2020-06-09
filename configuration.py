class Config:
    #AWS Information
    ACCESS_KEY = 'AKIAJI76SJZUFTLBJD2Q'
    SECRET_KEY = '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'
    INSTANCE_ID = 'i-08759302f6c0d4c94'
    ec2_region = "us-west-2"
    ec2_amis = ['ami-0e34e7b9ca0ace12d']
    ec2_keypair = 'minecraft_keypair'
    ec2_secgroups = ['minecraft']
    ec2_instancetype = 't3.small'

    #SSH Key Path
    SSH_KEY_FILE_PATH = './minecraft_keypair.pem'

    #Server Memory Size
    #This is default to no memory specification but can be: '-Xmx1024M -Xms1024M ' (KEEP TRAILING SPACE)
    MEMORY_ALLOCATION='' 

    SERVER_PASSWORD='gsm'