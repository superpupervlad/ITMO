from numpy import int32 as i32
from numpy import int16 as i16
from numpy import byte


class BlocksGroup():
    def __init__(self):
        self.blocks = []


class Block:
    def __init__(self, start_address):
        self.start_address = start_address

    def __iter__(self):
        return iter(self.__dict__.items())

    def write(self):
        for s in self:
            # write s
            print("TODO")


class SuperBlock(Block):
    def __init__(self, start_address):
        super().__init__(start_address)
        self.start_address = 1024
        self.s_inodes_count = i32(0)
        self.s_inodes_count = i32(0)
        self.s_blocks_count = i32(0)
        self.s_r_blocks_count = i32(0)
        self.s_free_blocks_count = i32(0)
        self.s_free_inodes_count = i32(0)
        self.s_first_data_block = i32(0)
        self.s_log_block_size = i32(0)
        self.s_log_frag_size = i32(0)
        self.s_blocks_per_group = i32(0)
        self.s_frags_per_group = i32(0)
        self.s_inodes_per_group = i32(0)
        self.s_mtime = i32(0)
        self.s_wtime = i32(0)
        self.s_mnt_count = i16(0)
        self.s_max_mnt_count = i16(0)
        self.s_magic = i16(0)
        self.s_state = i16(0)
        self.s_errors = i16(0)
        self.s_minor_rev_level = i16(0)
        self.s_lastcheck = i32(0)
        self.s_checkinterval = i32(0)
        self.s_creator_os = i32(0)
        self.s_rev_level = i32(0)
        self.s_def_resuid = i16(0)
        self.s_def_resgid = i16(0)
        # EXT2_DYNAMIC_REV Specific
        self.s_first_ino = i32(0)
        self.s_inode_size = i16(0)
        self.s_block_group_nr = i16(0)
        self.s_feature_compat = i32(0)
        self.s_feature_incompat = i32(0)
        self.s_feature_ro_compat = i32(0)
        # o 104 s 16
        self.s_uuid = "some string?"
        # o 120 s 16
        self.s_volume_name = "16 bytes volume name, mostly unusued. A valid volume name would consist of only " \
                             "ISO-Latin-1 characters and be 0 terminated. "
        # o 136 s 64
        self.s_last_mounted = "64 bytes directory path where the file system was last mounted. While not normally " \
                              "used, it could serve for auto-finding the mountpoint when not indicated on the command " \
                              "line. Again the path should be zero terminated for compatibility reasons. Valid path " \
                              "is constructed from ISO-Latin-1 characters. "
        # o 200 s 4
        self.s_algo_bitmap = "32bit value used by compression algorithms to determine the compression method(s) used."
        # Performance Hints
        self.s_prealloc_blocks = byte(0)
        self.s_prealloc_dir_blocks = byte(0)
        self.allignment = i16(0)  # o 206
        # Journaling Support
        self.s_journal_uuid = "16-byte value containing the uuid of the journal superblock. See Ext3 Journaling for " \
                              "more information. "
        self.s_journal_inum = i32(0)
        self.s_journal_dev = i32(0)
        self.s_last_orphan = i32(0)
        # Directory Indexing Support
        self.s_hash_seed = [i32(0)] * 4
        self.s_def_hash_version = byte(0)
        self. padding = [byte(0)] * 3  # reserved for future expansion
        # Other options
        self.s_default_mount_options = i32(0)
        self.s_first_meta_bg = i32(0)
        # o 264 s 760 - reserved for future revisions
        self.unused = [byte(0)] * 760


class BlockGroupDescriptor(Block):
    def __init__(self, start_address):
        super().__init__(start_address)
        self.start_address = start_address
        self.bg_block_bitmap = i32(0)
        self.bg_inode_bitmap = i32(0)
        self.bg_inode_table = i32(0)
        self.bg_free_blocks_count = i16(0)
        self.bg_free_inodes_count = i16(0)
        self.bg_used_dirs_count = i16(0)
        self.bg_pad = i16(0)
        self.bg_reserved = [byte(0)] * 12


class BlockBitmap(Block):
    def __init__(self, start_address):
        super().__init__(start_address)
        self.start_address = start_address  # bg_block_bitmap


class InodeBitmap(Block):
    def __init__(self, start_address):
        super().__init__(start_address)
        self.start_address = start_address  # bg_inode_bitmap
        # When the inode table is created, all the reserved inodes are marked as used. In revision 0 this is the
        # first 11 inodes.


class InodeTable(Block):
    def __init__(self, start_address):
        super().__init__(start_address)
        self.start_address = start_address  # bg_inode_table
        self.i_mode = i16(0)
        self.i_uid = i16(0)
        self.i_size = i32(0)
        self.i_atime = i32(0)
        self.i_ctime = i32(0)
        self.i_mtime = i32(0)
        self.i_dtime = i32(0)
        self.i_gid = i16(0)
        self.i_links_count = i16(0)
        self.i_blocks = i32(0)
        self.i_flags = i32(0)
        self.i_osd1 = i32(0)
        self.i_block = [i32(0)] * 15  # 12 blocks - direct block
        # 13th entry in this array is the block number of the first indirect block
        # 14th entry in this array is the block number of the first doubly-indirect block
        # 15th entry in this array is the block number of the triply-indirect block
        self.i_generation = i32(0)
        self.i_file_acl = i32(0)
        self.i_dir_acl = i32(0)
        self.i_faddr = i32(0)
        self.i_osd2 = [byte(0)] * 12  # 96 bit OS dependant


#  Locate in which block group inode is
#  block group = (inode - 1) / s_inodes_per_group
#  Locate index of inode in appropriate block
#  local inode index = (inode - 1) % s_inodes_per_group


class Image:
    def __init__(self):
        self.offset = (0).to_bytes(1, "big") * 1024
        self.superblock = SuperBlock(0)
