"""initial database migration

Revision ID: b086bfe93563
Revises: 
Create Date: 2025-04-11 15:32:51.648256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b086bfe93563'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workflow_runs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('workflow_name', sa.String(), nullable=False),
    sa.Column('branch_name', sa.String(), nullable=False),
    sa.Column('network_name', sa.String(), nullable=False),
    sa.Column('triggered_at', sa.DateTime(), nullable=False),
    sa.Column('inputs', sa.JSON(), nullable=False),
    sa.Column('run_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workflow_runs_id'), 'workflow_runs', ['id'], unique=False)
    op.create_table('base_deployments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deployment_type', sa.Enum('NETWORK', 'CLIENT', name='deploymenttype'), nullable=False),
    sa.Column('workflow_run_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('triggered_at', sa.DateTime(), nullable=False),
    sa.Column('run_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('region', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['workflow_run_id'], ['workflow_runs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_base_deployments_id'), 'base_deployments', ['id'], unique=False)
    op.create_table('client_deployments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ant_version', sa.String(), nullable=True),
    sa.Column('branch', sa.String(), nullable=True),
    sa.Column('repo_owner', sa.String(), nullable=True),
    sa.Column('chunk_size', sa.Integer(), nullable=True),
    sa.Column('client_vm_count', sa.Integer(), nullable=False),
    sa.Column('client_vm_size', sa.String(), nullable=False),
    sa.Column('client_env', sa.String(), nullable=True),
    sa.Column('evm_network_type', sa.String(), nullable=False),
    sa.Column('evm_data_payments_address', sa.String(), nullable=True),
    sa.Column('evm_payment_token_address', sa.String(), nullable=True),
    sa.Column('evm_rpc_url', sa.String(), nullable=True),
    sa.Column('network_id', sa.Integer(), nullable=True),
    sa.Column('related_pr', sa.Integer(), nullable=True),
    sa.Column('provider', sa.String(), nullable=False),
    sa.Column('wallet_secret_key', sa.String(), nullable=True),
    sa.Column('environment_type', sa.String(), nullable=False),
    sa.Column('disable_download_verifier', sa.Boolean(), nullable=True),
    sa.Column('disable_performance_verifier', sa.Boolean(), nullable=True),
    sa.Column('disable_random_verifier', sa.Boolean(), nullable=True),
    sa.Column('disable_telegraf', sa.Boolean(), nullable=True),
    sa.Column('disable_uploaders', sa.Boolean(), nullable=True),
    sa.Column('expected_hash', sa.String(), nullable=True),
    sa.Column('expected_size', sa.String(), nullable=True),
    sa.Column('file_address', sa.String(), nullable=True),
    sa.Column('initial_gas', sa.String(), nullable=True),
    sa.Column('initial_tokens', sa.String(), nullable=True),
    sa.Column('max_uploads', sa.Integer(), nullable=True),
    sa.Column('network_contacts_url', sa.String(), nullable=True),
    sa.Column('peer', sa.String(), nullable=True),
    sa.Column('uploaders_count', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['base_deployments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comparisons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ref_id', sa.Integer(), nullable=False),
    sa.Column('deployment_type', sa.Enum('NETWORK', 'CLIENT', name='deploymenttype'), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('thread_link', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('ref_label', sa.String(), nullable=True),
    sa.Column('passed', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['ref_id'], ['base_deployments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comparisons_id'), 'comparisons', ['id'], unique=False)
    op.create_table('network_deployments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ant_version', sa.String(), nullable=True),
    sa.Column('antnode_version', sa.String(), nullable=True),
    sa.Column('antctl_version', sa.String(), nullable=True),
    sa.Column('branch', sa.String(), nullable=True),
    sa.Column('repo_owner', sa.String(), nullable=True),
    sa.Column('chunk_size', sa.Integer(), nullable=True),
    sa.Column('antnode_features', sa.String(), nullable=True),
    sa.Column('peer_cache_node_count', sa.Integer(), nullable=True),
    sa.Column('generic_node_count', sa.Integer(), nullable=False),
    sa.Column('private_node_count', sa.Integer(), nullable=True),
    sa.Column('enable_downloaders', sa.Boolean(), nullable=True),
    sa.Column('uploader_count', sa.Integer(), nullable=True),
    sa.Column('peer_cache_vm_count', sa.Integer(), nullable=True),
    sa.Column('generic_vm_count', sa.Integer(), nullable=False),
    sa.Column('private_vm_count', sa.Integer(), nullable=True),
    sa.Column('client_vm_count', sa.Integer(), nullable=True),
    sa.Column('peer_cache_node_vm_size', sa.String(), nullable=True),
    sa.Column('generic_node_vm_size', sa.String(), nullable=False),
    sa.Column('private_node_vm_size', sa.String(), nullable=True),
    sa.Column('client_vm_size', sa.String(), nullable=True),
    sa.Column('evm_network_type', sa.String(), nullable=False),
    sa.Column('rewards_address', sa.String(), nullable=False),
    sa.Column('max_log_files', sa.Integer(), nullable=True),
    sa.Column('max_archived_log_files', sa.Integer(), nullable=True),
    sa.Column('evm_data_payments_address', sa.String(), nullable=True),
    sa.Column('evm_payment_token_address', sa.String(), nullable=True),
    sa.Column('evm_rpc_url', sa.String(), nullable=True),
    sa.Column('related_pr', sa.Integer(), nullable=True),
    sa.Column('network_id', sa.Integer(), nullable=True),
    sa.Column('client_env', sa.String(), nullable=True),
    sa.Column('node_env', sa.String(), nullable=True),
    sa.Column('full_cone_private_node_count', sa.Integer(), nullable=True),
    sa.Column('full_cone_private_vm_count', sa.Integer(), nullable=True),
    sa.Column('full_cone_nat_gateway_vm_size', sa.String(), nullable=True),
    sa.Column('symmetric_private_node_count', sa.Integer(), nullable=True),
    sa.Column('symmetric_private_vm_count', sa.Integer(), nullable=True),
    sa.Column('symmetric_nat_gateway_vm_size', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['base_deployments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('smoke_test_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deployment_id', sa.Integer(), nullable=False),
    sa.Column('results', sa.JSON(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['deployment_id'], ['base_deployments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_smoke_test_results_id'), 'smoke_test_results', ['id'], unique=False)
    op.create_table('client_smoke_test_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deployment_id', sa.Integer(), nullable=False),
    sa.Column('results', sa.JSON(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['deployment_id'], ['client_deployments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_smoke_test_results_id'), 'client_smoke_test_results', ['id'], unique=False)
    op.create_table('comparison_deployments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comparison_id', sa.Integer(), nullable=False),
    sa.Column('deployment_id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['comparison_id'], ['comparisons.id'], ),
    sa.ForeignKeyConstraint(['deployment_id'], ['base_deployments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comparison_deployments')
    op.drop_index(op.f('ix_client_smoke_test_results_id'), table_name='client_smoke_test_results')
    op.drop_table('client_smoke_test_results')
    op.drop_index(op.f('ix_smoke_test_results_id'), table_name='smoke_test_results')
    op.drop_table('smoke_test_results')
    op.drop_table('network_deployments')
    op.drop_index(op.f('ix_comparisons_id'), table_name='comparisons')
    op.drop_table('comparisons')
    op.drop_table('client_deployments')
    op.drop_index(op.f('ix_base_deployments_id'), table_name='base_deployments')
    op.drop_table('base_deployments')
    op.drop_index(op.f('ix_workflow_runs_id'), table_name='workflow_runs')
    op.drop_table('workflow_runs')
    # ### end Alembic commands ### 